import configparser

# Specify the path to the INI file containing user sections
ini_file_path = 'env/.env'

# Read the INI file
config = configparser.ConfigParser()
config.read(ini_file_path)



# from pydantic import BaseSettings, EmailStr


# class Settings(BaseSettings):
#     DATABASE_PORT: int
#     POSTGRES_PASSWORD: str
#     POSTGRES_USER: str
#     POSTGRES_DB: str
#     POSTGRES_HOST: str
#     POSTGRES_HOSTNAME: str

#     JWT_PUBLIC_KEY: str
#     JWT_PRIVATE_KEY: str
#     REFRESH_TOKEN_EXPIRES_IN: int
#     ACCESS_TOKEN_EXPIRES_IN: int
#     JWT_ALGORITHM: str

#     CLIENT_ORIGIN: str

#     VERIFICATION_SECRET: str

#     MAIL_USERNAME: str
#     MAIL_PASSWORD: str
#     MAIL_FROM: str
#     MAIL_PORT: int
#     MAIL_SERVER: str
#     MAIL_STARTTLS: bool
#     MAIL_SSL_TLS: bool
#     USE_CREDENTIALS: bool
#     VALIDATE_CERTS: bool
    
#     # EMAIL_HOST: str
#     # EMAIL_PORT: int
#     # EMAIL_USERNAME: str
#     # EMAIL_PASSWORD: str
#     # EMAIL_FROM: EmailStr

#     class Config:
#         env_file = './.env'


# settings = Settings()
