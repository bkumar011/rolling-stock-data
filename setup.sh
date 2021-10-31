mkdir -p ~/.streamlit/
echo "
[general]n
email = "bkumar011@gmail.com"n
" > ~/.streamlit/credentials.toml
echo "
[server]n
headless = truen
enableCORS=falsen
port = $PORTn
" > ~/.streamlit/config.toml