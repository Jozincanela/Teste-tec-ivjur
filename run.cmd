@echo off

set AMBIENTE_VIRTUAL=env
cd .\Questao2\
python -m venv %AMBIENTE_VIRTUAL%
echo Ambiente virtual %AMBIENTE_VIRTUAL% criado com sucesso.
call .\%AMBIENTE_VIRTUAL%\Scripts\activate
pip install fastapi
pip install uvicorn
pip install SQLAlchemy
echo Libs instaladas
echo Ambiente virtual para a Questao2 foi criado!

set AMBIENTE_VIRTUAL=env
cd ..\Questao3\
python -m venv %AMBIENTE_VIRTUAL%
echo Ambiente virtual %AMBIENTE_VIRTUAL% criado com sucesso.
call .\%AMBIENTE_VIRTUAL%\Scripts\activate
pip install fastapi
pip install uvicorn
pip install requests
echo Libs instaladas
echo Ambiente virtual para a Questao3 foi criado!
