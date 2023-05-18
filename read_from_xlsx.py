import pandas
from src.models.emolument_db import Emolument
from src.database.dbconfig import session

columns_association = {
    "CODIGO ATO": "codigo",
    "EMOLUMENTOS": "emolumentos",
    "DESCRICAO": "descricao",
    "TIPO_SELO": "tipo_selo",
    "FERMOJU": "fermoju",
    "SELO": "valor_selo",
    "SUB_TOTAL": "subtotal",
    "FAADEP": "faadep",
    "FRMMP": "frmmp",
    "TOTAL": "total",
}


excel_data = pandas.read_excel("./public/tabela.xlsx")
excel_data = excel_data.rename(mapper=columns_association, axis="columns")


with session:
    for row in excel_data.iterrows():
        row_data = row[1]

        new_emolument = Emolument(**row_data)
        session.add(new_emolument)

    session.commit()
