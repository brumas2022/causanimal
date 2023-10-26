import streamlit as st
import psycopg2



st.set_page_config(page_title="Caes abrigados")
def apresenta():
    try:
        
        connection = psycopg2.connect(
                   host='db.ibhcxtnwnonsnycfgjay.supabase.co',
                   user='postgres',
                   password='Hoje#estamos#fortes#como#geleia',
                   database='postgres',
                   port= '5432'
        )
        st.write("conexao exitosa")
        cursor = connection.cursor()
        
        
        comando = f"""SELECT * FROM caninos"""
        cursor.execute(comando)
        resultado = cursor.fetchall()
    except Exception as ex:
            st.write(ex)

    st.dataframe(resultado)

def inserir(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12):
    try:
     connection = psycopg2.connect(
               host='db.ibhcxtnwnonsnycfgjay.supabase.co',
               user='postgres',
               password='Hoje#estamos#fortes#como#geleia',
               database='postgres',
               port='5432'
     )
     st.write("conexao exitosa")

     cursor = connection.cursor()



     comando = f"""INSERT INTO caninos (nome, genero, entrada, castracao, vacina1, vacina2, vacina3, adocao, morte, quem_adotou, foto, historico) VALUES ('{a1}', '{a2}', '{a3}', '{a4} ', '{a5}', '{a6}', '{a7}', '{a8}', '{a9}', '{a10} ', '{a11}', '{a12} ')"""
     

     cursor.execute(comando)
     connection.commit()
     st.text("Cadastro efetuado com sucesso")
     cursor.close()
     connection.close()

          
    except Exception as ex:
            st.write(ex)

def captura():
    with st.form("Caputar dados", clear_on_submit=True):
        a1 = st.text_input("Nome do câo")
        a2 = st.text_input("Genero do cão")
        a3 = st.date_input("Data da entrada", value=None)
        a4 = st.date_input("Data da castração")
        a5 = st.date_input("Data da primeira vacina")
        a6 = st.date_input("Data da segunda vacina")
        a7 = st.date_input("Data da terceira vacina")
        a8 = st.date_input("Data da adocao")
        a9 = st.date_input("Data da morte")
        a10 = st.text_input("Quem adotou")
        a11 = st.text_input("Escolha a foto")
        a12 = st.text_input("Historico do caozinho")
        enviar = st.form_submit_button()
        if enviar:
            inserir(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12)
        
def consulta():
    
    nome1 = st.selectbox("Escolha o nome", ("Bob", "Gorda", "Mosquito"))
                       
    
    try:
        
        connection = psycopg2.connect(
                   host='db.ibhcxtnwnonsnycfgjay.supabase.co',
                   user='postgres',
                   password='Hoje#estamos#fortes#como#geleia',
                   database='postgres',
                   port= '5432'
        )
        st.write("conexao exitosa")
        cursor = connection.cursor()
        
        
        comando = f"""SELECT * FROM caninos WHERE nome='{nome1}'"""
        cursor.execute(comando)
        resultado = cursor.fetchone()
    except Exception as ex:
            st.write(ex)

    st.write(resultado[1])
    st.write(resultado[2])
    st.write(resultado[3])
    st.image(resultado[12])
    st.write(resultado[13])
    


st.title("Cadastro dos caes")
st.divider()
selecao = st.selectbox("Escolha o modulo", ("CADASTRAR", "ATUALIZAR", "REMOVER", "RELATORIO"))
if selecao == "CADASTRAR":
    captura()
    
elif selecao == "ATUALIZAR":
    consulta()
    
elif selecao == "REMOVER":
    st.text("Este modulo ainda está em construção")
    
elif selecao == "RELATORIO":
    apresenta()
    
    
