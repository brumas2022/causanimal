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
        
        
        comando = f"""SELECT * FROM caninos WHERE genero='macho'"""
        cursor.execute(comando)
        resultado = cursor.fetchall()
        st.markdown(":sunglasses: O numero de machos é : ")
        st.markdown(len(resultado))

        comando = f"""SELECT * FROM caninos WHERE genero='femeas'"""
        cursor.execute(comando)
        resultado = cursor.fetchall()
        st.markdown(":sunglasses: O numero de femeas é : "+len(resultado))

        comando = f"""SELECT * FROM caninos"""
        cursor.execute(comando)
        resultado = cursor.fetchall()
        st.markdown(":sunglasses: O numero de total é : ", len(resultado))
        
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
        col = st.columns((1,1))
        a1 = col[0].text_input("Nome do câo")
        a2 = col[0].text_input("Genero do cão")
        a3 = col[0].date_input("Data da entrada")
        a4 = col[0].date_input("Data da castração")
        a5 = col[0].date_input("Data da primeira vacina")
        a6 = col[0].date_input("Data da segunda vacina")
        a7 = col[1].date_input("Data da terceira vacina")
        a8 = col[1].date_input("Data da adocao")
        a9 = col[1].date_input("Data da morte")
        a10 = col[1].text_input("Quem adotou")
        a11 = col[1].text_input("Escolha a foto")
        a12 = col[1].text_input("Historico do caozinho")
        enviar = st.form_submit_button()
        if enviar:
            inserir(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12)
        
def consulta():
    
    nome1 = st.selectbox("Escolha o nome", ("Bob", "Gorda", "Mosquito", "Baby", "Jhony"))
                       
    
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
        
    cols = st.columns((0.75,0.25))
    ##a = cols[1].markdown(resultado[1])
    b = cols[1].write(resultado[2])
    c = cols[1].write(resultado[3])
    d = cols[0].image(resultado[12])
    e = cols[1].write(resultado[13])
    


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
    
    
