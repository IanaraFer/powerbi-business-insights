"""
HTML to PDF Converter Script
Simple script to convert HTML files to PDF using available libraries
"""

def convert_html_to_pdf():
    import sys
    import os
    
    # Try different PDF conversion methods
    methods = []
    
    # Method 1: Try using reportlab
    try:
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import letter, A4
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
        from reportlab.lib.styles import getSampleStyleSheet
        from reportlab.lib.units import inch
        import re
        methods.append("reportlab")
        print("✓ ReportLab available")
    except ImportError:
        print("✗ ReportLab not available")
    
    # Method 2: Try using weasyprint
    try:
        import weasyprint
        methods.append("weasyprint")
        print("✓ WeasyPrint available")
    except (ImportError, OSError) as e:
        print("✗ WeasyPrint not available")
    
    # Method 3: Try using pdfkit
    try:
        import pdfkit
        methods.append("pdfkit")
        print("✓ PDFKit available")
    except ImportError:
        print("✗ PDFKit not available")
    
    # Read the HTML file
    html_file = "project-export.html"
    pdf_file = "project-export.pdf"
    
    if not os.path.exists(html_file):
        print(f"❌ HTML file '{html_file}' not found")
        return False
    
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    print(f"📄 Converting {html_file} to {pdf_file}...")
    
    # Try WeasyPrint first (if available)
    if "weasyprint" in methods:
        try:
            from weasyprint import HTML
            HTML(string=html_content).write_pdf(pdf_file)
            print(f"✅ Successfully converted using WeasyPrint!")
            return True
        except Exception as e:
            print(f"❌ WeasyPrint failed: {e}")
    
    # Try PDFKit
    if "pdfkit" in methods:
        try:
            pdfkit.from_string(html_content, pdf_file)
            print(f"✅ Successfully converted using PDFKit!")
            return True
        except Exception as e:
            print(f"❌ PDFKit failed: {e}")
    
    # Fallback: Create a simple text-based PDF using ReportLab
    if "reportlab" in methods:
        try:
            from bs4 import BeautifulSoup
            print("ℹ️  Falling back to ReportLab with basic HTML parsing...")
            
            # Parse HTML to extract text content
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.extract()
            
            # Get text content
            text = soup.get_text()
            
            # Clean up text
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = '\n'.join(chunk for chunk in chunks if chunk)
            
            # Create PDF
            doc = SimpleDocTemplate(pdf_file, pagesize=A4)
            styles = getSampleStyleSheet()
            story = []
            
            # Split text into paragraphs
            paragraphs = text.split('\n\n')
            
            for para_text in paragraphs[:50]:  # Limit to first 50 paragraphs
                if para_text.strip():
                    # Check if it looks like a heading
                    if len(para_text) < 100 and para_text.isupper():
                        para = Paragraph(para_text, styles['Heading1'])
                    elif para_text.startswith('#'):
                        para = Paragraph(para_text.replace('#', ''), styles['Heading2'])
                    else:
                        para = Paragraph(para_text, styles['Normal'])
                    story.append(para)
                    story.append(Spacer(1, 12))
            
            doc.build(story)
            print(f"✅ Successfully converted using ReportLab (text-only)!")
            return True
            
        except Exception as e:
            print(f"❌ ReportLab failed: {e}")
    
    print("❌ All conversion methods failed. Consider using browser Print to PDF.")
    return False

if __name__ == "__main__":
    convert_html_to_pdf()