import streamlit_authenticator as stauth

# 正しい形でパスワードのハッシュ化を行う
passwords = ['tintin']
hashed_passwords = stauth.Hasher(passwords).generate()

print(hashed_passwords)

