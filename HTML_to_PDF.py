import sys
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright
from pypdf import PdfReader, PdfWriter


def drop_last_pdf_page(pdf_path: Path) -> None:
    reader = PdfReader(str(pdf_path))
    writer = PdfWriter()

    # Copy all but the last page
    for i in range(max(0, len(reader.pages) - 1)):
        writer.add_page(reader.pages[i])

    tmp = pdf_path.with_suffix(".tmp.pdf")
    with open(tmp, "wb") as f:
        writer.write(f)

    tmp.replace(pdf_path)


PDF_FOOTER_LINE_CSS = r"""
@media print {
  .reveal .pdf-page {
    position: relative;
  }

  /* ---------- HEADER ---------- */

  .pdf-header-center {
    position: absolute;
    top: 20px;
    left: 0;
    right: 0;
    text-align: center;
    font-size: 13px;
    letter-spacing: 0.10em;
    color: #444;
    opacity: 0.85;
    text-transform: uppercase;
    pointer-events: none;
  }

  /* ---------- FOOTER ---------- */

  /* horizontal footer line */
  .reveal .pdf-page::after {
    content: "";
    position: absolute;
    left: 40px;
    right: 40px;
    bottom: 40px;
    height: 0.75px;
    background: #444;
    opacity: 0.55;
  }

  /* right footer text */
  .reveal .pdf-page::before {
    content: "Spring 2026";
    position: absolute;
    right: 40px;
    bottom: 20px;
    font-size: 11px;
    letter-spacing: 0.06em;
    color: #444;
    opacity: 0.75;
    text-transform: uppercase;
  }

  /* left footer text */
  .pdf-footer-left {
    position: absolute;
    left: 40px;
    bottom: 20px;
    font-size: 11px;
    letter-spacing: 0.06em;
    color: #444;
    opacity: 0.75;
    text-transform: uppercase;
    pointer-events: none;
  }

  /* center footer page number */
  .pdf-footer-center {
    position: absolute;
    left: 0;
    right: 0;
    bottom: 20px;
    text-align: center;
    font-size: 11px;
    letter-spacing: 0.06em;
    color: #444;
    opacity: 0.75;
    pointer-events: none;
  }
}
"""


async def html_to_pdf(html_path: str, pdf_path: str):
    html_file = Path(html_path).resolve()
    url = html_file.as_uri() + "?print-pdf"  # reveal.js print mode

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        await page.goto(url, wait_until="networkidle")

        # Inject PDF-only footer/header styling
        await page.add_style_tag(content=PDF_FOOTER_LINE_CSS)

        # Inject header, left footer, and centered page numbers
        await page.evaluate(
            """
            () => {
              const pages = Array.from(
                document.querySelectorAll('.reveal .pdf-page')
              );
              const total = pages.length;


              pages.forEach((page, i) => {

                /* ---- HEADER (center) ---- */
                if (!page.querySelector('.pdf-header-center')) {
                  const header = document.createElement('div');
                  header.className = 'pdf-header-center';
                  header.textContent = 'Lecture 3: 01/30';
                  page.appendChild(header);
                }

                /* ---- FOOTER (left) ---- */
                if (!page.querySelector('.pdf-footer-left')) {
                  const footer = document.createElement('div');
                  footer.className = 'pdf-footer-left';
                  footer.textContent = 'CEE6501 – Matrix Structural Analysis';
                  page.appendChild(footer);
                }

                /* ---- FOOTER (center: page number) ---- */
                if (!page.querySelector('.pdf-footer-center')) {
                  const num = document.createElement('div');
                  num.className = 'pdf-footer-center';
                  num.textContent = `${i + 1} / ${total}`;
                  page.appendChild(num);
                }

              });
            }
            """
        )

        # Give reveal/layout a moment to settle
        await page.wait_for_timeout(250)

        await page.pdf(
            path=str(Path(pdf_path).resolve()),
            print_background=True,
            format="Letter",  # or "A4"
            margin={
                "top": "0in",
                "right": "0in",
                "bottom": "0in",
                "left": "0in",
            },
            prefer_css_page_size=True,
        )
        await browser.close()

        # Always remove the final page
        drop_last_pdf_page(Path(pdf_path))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python HTML_to_PDF.py path/to/file.slides.html")
        sys.exit(1)

    html_file = Path(sys.argv[1]).resolve()
    if not html_file.exists():
        print(f"ERROR: File not found: {html_file}")
        sys.exit(1)

    # Output PDF name: remove ".slides" from filename
    pdf_file = html_file.with_name(
        html_file.name.replace(".slides.html", ".pdf")
    )

    asyncio.run(html_to_pdf(str(html_file), str(pdf_file)))
