import streamlit as st
import psycopg2
import pandas as pd




st.set_page_config(page_title="Caes abrigados", layout="wide")

password=0
while True:
   login = st.sidebar.text_input("Digite o login")
   password = st.sidebar.text_input("Digite a senha")
   if password=="jacare":
      break
   else:
      st.sidebar.write("Tente outra vez")
   

senha = st.sidebar.selectbox(
    "Escolha um deles para continuar",
    ("Janis", "Home phone", "Mobile phone")
)

if senha=="Janis":
    st.sidebar.markdown(":green[Janis esta de olho em voce]")
    st.sidebar.image("IMG_20230929_132220668~2.jpg")
if senha=="Home phone":
    st.sidebar.markdown(":blue[Voce escolheu o home phone]")   



def apresenta():
    try:
        
        connection = psycopg2.connect(
                   host='aws-0-sa-east-1.pooler.supabase.com',
                   user='postgres.ibhcxtnwnonsnycfgjay',
                   password='Hoje#estamos#firmes#como#geleia',
                   database='postgres',
                   port='5432'
                   ##host='db.ibhcxtnwnonsnycfgjay.supabase.co',
                   ##user='postgres',
                   ##password='Hoje#estamos#fortes#como#geleia',
                   ##database='postgres',
                   ##port= '5432'
        )
        st.write("conexao exitosa")
        cursor = connection.cursor()
        
        
        comando = f"""SELECT * FROM caninos WHERE genero='macho' and vivo=True"""
        cursor.execute(comando)
        resultado = cursor.fetchall()
        st.markdown(":dog2: O numero de machos é : "+str(len(resultado)))

        comando = f"""SELECT * FROM caninos WHERE genero='femea' and vivo=True"""
        cursor.execute(comando)
        resultado = cursor.fetchall()
        st.markdown(":dog: O numero de femeas é : "+ str(len(resultado)))

        comando = f"""SELECT * FROM caninos WHERE castrado=True"""
        cursor.execute(comando)
        resultado = cursor.fetchall()
        st.markdown(":sunglasses: :sunglasses: O numero de castrados é : "+str(len(resultado)))
       
        comando = f"""SELECT * FROM caninos WHERE vivo=True"""
        cursor.execute(comando)
        resultado = cursor.fetchall()
        st.markdown(":sunglasses: :sunglasses: O numero de total é : "+str(len(resultado)))

        
        
    except Exception as ex:
            st.write(ex)
    
    #st.column_config.ImageColumn(label="12", width="small", help=None)
    #st.dataframe(resultado)
    st.data_editor(resultado,column_config={"12": st.column_config.ImageColumn("Preview Image", help="Streamlit app preview screenshots")}, hide_index=True,)

def inserir(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12):
    try:
     connection = psycopg2.connect(
               host='aws-0-sa-east-1.pooler.supabase.com',
               user='postgres.ibhcxtnwnonsnycfgjay',
               password='Hoje#estamos#firmes#como#geleia',
               database='postgres',
               port='5432'


        
               ##host='db.ibhcxtnwnonsnycfgjay.supabase.co',
               ##user='postgres',
               ##password='Hoje#estamos#fortes#como#geleia',
               ##database='postgres',
               ##port='5432'
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
    
    ##nome1 = st.radio("Escolha o nome", ("Bob", "Gorda", "Mosquito", "Baby", "Jhony", "Margarete", "Vira lata", "Magrelo", "Jair", "Branquelo", "Boca preta", "Betina"))
    cols = st.columns((1,1,1))              
    
    try:
        
        connection = psycopg2.connect(
                   host='aws-0-sa-east-1.pooler.supabase.com',
                   user='postgres.ibhcxtnwnonsnycfgjay',
                   password='Hoje#estamos#firmes#como#geleia',
                   database='postgres',
                   port='5432'
            
                   ##ANTIGA CONFIGURACAO DO DATABASE
                   ##host='db.ibhcxtnwnonsnycfgjay.supabase.co',
                   ##user='postgres',
                   ##password='Hoje#estamos#fortes#como#geleia',
                   ##database='postgres',
                   ##port= '5432'
        )

        cursor = connection.cursor()
       
        caozinho = f"""SELECT nome FROM caninos"""
        cursor.execute(caozinho)
        nome2 = cursor.fetchall()
        df = pd.DataFrame(nome2)
        nome2 = df[0].tolist()
        
        nome1 = cols[0].radio("Escolha o caozinho", (nome2))
        
        
        
        comando = f"""SELECT * FROM caninos WHERE nome='{nome1}'"""
        cursor.execute(comando)
        resultado = cursor.fetchone()
    except Exception as ex:
            st.write(ex)
        
    if resultado[14]==True:
       cols[2].markdown("***Animal castrado(a)***")
    
    cols[2].markdown("Nome : "+resultado[2])
    cols[2].markdown("Genero : "+resultado[3])
    cols[1].image(resultado[12])
    cols[2].markdown("Data entrada :"+resultado[4].strftime("%d/%m/%y"))
    cols[2].markdown("Historia :"+resultado[13])
    


st.title("Cadastro dos caes")
st.divider()
selecao = st.selectbox("Escolha o modulo", ("CADASTRAR", "CONSULTAR", "REMOVER", "RELATORIO"))
if selecao == "CADASTRAR":
    captura()
    
elif selecao == "CONSULTAR":
    consulta()
    
elif selecao == "REMOVER":
    st.text("Este modulo ainda está em construção")
    
elif selecao == "RELATORIO":
    apresenta()
    
    
