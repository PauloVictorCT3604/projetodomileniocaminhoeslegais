from fastapi import FastAPI
from controllers import veiculo_controller, entrega_controller, motorista_controller, base_controller

app = FastAPI()

app.include_router(veiculo_controller.roteador, prefix="/api")
app.include_router(entrega_controller.roteador, prefix="/api")
app.include_router(motorista_controller.roteador, prefix="/api")
app.include_router(base_controller.roteador, prefix="/api")
