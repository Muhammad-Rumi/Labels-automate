from docxtpl import DocxTemplate
import pandas as pd 
print('import successful')
df = pd.read_csv('test.csv')
print(df.T)

# data = None

# doc = DocxTemplate('template.docx')
# doc.render(data)
# doc.save('test.docx')