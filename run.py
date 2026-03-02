from app.database import engine
from app.models import Base

print("Criando tabelas..")
Base.metadata.create_all(engine)
print("Tabelas criadas com sucesso.")