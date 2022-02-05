proposal = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Варианты выбора</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="http://localhost:8080/static/css/style.css">
</head>
<body>
    <div class="container">
        <h1>Моё предложение: {}!</h1>
        <div class="col coral">Это красивая планета!</div>
        <div class="col green">Это просто замечательная планета!</div>
        <div class="col pink">Это очень перспективная для развития жизни планета!</div>
    </div>
</body>
</html>
"""

result = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Варианты выбора</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="http://localhost:8080/static/css/style.css">
</head>
<body>
    <div class="container">
        <h1>Результаты отбора</h1>
        <h2>Претендента на участие в миссии {}:</h2>
        <div class="col green">Поздравляем! Ваш рейтинг после {} этапа отбора</div>
        <div class="col coral">составляет {}!</div>
        <div class="col yellow">Удачи!</div>
    </div>
</body>
</html>
"""