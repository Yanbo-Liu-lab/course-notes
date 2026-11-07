"""Open a docx in headless LibreOffice, refresh its TOC, then save docx + pdf.

usage: uno_export.py <in.docx> <out.docx> <out.pdf>
"""
import os
import subprocess
import sys
import time

import uno
from com.sun.star.beans import PropertyValue

PORT = 2012
PROFILE = 'file:///tmp/lo_profile_claude_export'


def connect():
    local = uno.getComponentContext()
    resolver = local.ServiceManager.createInstanceWithContext(
        'com.sun.star.bridge.UnoUrlResolver', local)
    for _ in range(60):
        try:
            return resolver.resolve(
                f'uno:socket,host=127.0.0.1,port={PORT};urp;StarOffice.ComponentContext')
        except Exception:
            time.sleep(1)
    raise RuntimeError('cannot connect to LibreOffice')


def prop(name, value):
    p = PropertyValue()
    p.Name = name
    p.Value = value
    return p


def main():
    src, out_docx, out_pdf = (os.path.abspath(p) for p in sys.argv[1:4])
    proc = subprocess.Popen([
        'soffice', '--headless', '--invisible', '--norestore', '--nologo',
        f'-env:UserInstallation={PROFILE}',
        f'--accept=socket,host=127.0.0.1,port={PORT};urp;StarOffice.ComponentContext',
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        ctx = connect()
        desktop = ctx.ServiceManager.createInstanceWithContext(
            'com.sun.star.frame.Desktop', ctx)
        doc = desktop.loadComponentFromURL(
            uno.systemPathToFileUrl(src), '_blank', 0, (prop('Hidden', True),))

        indexes = doc.getDocumentIndexes()
        for i in range(indexes.getCount()):
            indexes.getByIndex(i).update()
        doc.refresh()
        print(f'updated {indexes.getCount()} index(es)')

        doc.storeToURL(uno.systemPathToFileUrl(out_docx),
                       (prop('FilterName', 'MS Word 2007 XML'),))
        doc.storeToURL(uno.systemPathToFileUrl(out_pdf),
                       (prop('FilterName', 'writer_pdf_Export'),))
        doc.close(False)
        print('saved', out_docx)
        print('saved', out_pdf)
    finally:
        try:
            desktop.terminate()
        except Exception:
            pass
        proc.wait(timeout=30)


if __name__ == '__main__':
    main()
