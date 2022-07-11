from __future__ import print_function
from mailmerge import MailMerge
from datetime import date

template = "SHIPPING_INSTRUCTION_TEMPLATE.docx"
document = MailMerge(template)

print(document.get_merge_fields())