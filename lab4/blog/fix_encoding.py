import os

# Создаем папки если их нет
os.makedirs('articles/templates', exist_ok=True)
os.makedirs('articles/static/css', exist_ok=True)
os.makedirs('articles/static/img', exist_ok=True)

# Создаем archive.html
with open('articles/templates/archive.html', 'w', encoding='utf-8') as f:
    f.write('''<!DOCTYPE html>
<html>
<head>
    <title>Архив статей</title>
    {% load static %}
    <link rel="stylesheet" href="{% static 'css/article.css' %}">
</head>
<body class="archive">
    <div class="header">
        <img src="{% static 'img/logo.png' %}" alt="Логотип">
    </div>
    <div class="archive">
        {% for post in posts %}
        <div class="one-post">
            <h2 class="post-title">
                <a href="{% url 'get_article' article_id=post.id %}">{{ post.title }}</a>
            </h2>
            <div class="article-info">
                <div class="article-author">{{ post.author.username }}</div>
                <div class="article-created-date">{{ post.created_date }}</div>
            </div>
            <p class="article-text">{{ post.get_excerpt }}</p>
        </div>
        {% endfor %}
    </div>
</body>
</html>''')

# Создаем article.html
with open('articles/templates/article.html', 'w', encoding='utf-8') as f:
    f.write('''<!DOCTYPE html>
<html>
<head>
    <title>{{ post.title }}</title>
    {% load static %}
    <link rel="stylesheet" href="{% static 'css/article.css' %}">
</head>
<body class="article">
    <div class="header">
        <img src="{% static 'img/logo.png' %}" alt="Логотип">
    </div>
    <div class="content">
        <div class="one-post">
            <h2 class="post-title">{{ post.title }}</h2>
            <div class="article-info">
                <div class="article-author">{{ post.author.username }}</div>
                <div class="article-created-date">{{ post.created_date }}</div>
            </div>
            <div class="article-text">
                {{ post.text|linebreaks }}
            </div>
        </div>
        <div class="link-back">
            <a href="{% url 'archive' %}">Все записи</a>
        </div>
    </div>
</body>
</html>''')

# Создаем article.css
with open('articles/static/css/article.css', 'w', encoding='utf-8') as f:
    f.write('''body {
    background: #1abc9c;
    font-family: Tahoma, Arial, sans-serif;
    color: #ffffff;
    margin: 0;
    padding: 0;
}

.header {
    text-align: center;
    padding: 20px 0;
}

.header img {
    display: block;
    width: 318px;
    margin-left: auto;
    margin-right: auto;
}

.archive {
    width: 960px;
    margin-left: auto;
    margin-right: auto;
}

.one-post {
    background: rgba(255, 255, 255, 0.1);
    margin: 20px 0;
    padding: 20px;
    border-radius: 10px;
}

.post-title {
    margin-top: 0;
    margin-bottom: 10px;
}

.post-title a {
    color: #ffffff;
    text-decoration: none;
}

.post-title a:hover {
    text-decoration: underline;
}

.article-info {
    display: flex;
    justify-content: space-between;
    margin-bottom: 15px;
    font-size: 14px;
    color: #e0e0e0;
}

.article-author {
    font-weight: bold;
}

.article-created-date {
    font-style: italic;
}

.article-text {
    line-height: 1.6;
    margin-bottom: 0;
}

.article .content {
    width: 960px;
    margin-left: auto;
    margin-right: auto;
}

.article .one-post {
    background: rgba(255, 255, 255, 0.1);
    padding: 30px;
    border-radius: 10px;
    margin-bottom: 20px;
}

.article .article-text {
    font-size: 16px;
    line-height: 1.8;
    margin-top: 20px;
}

.link-back {
    text-align: center;
    margin-top: 30px;
}

.link-back a {
    color: #ffffff;
    text-decoration: none;
    font-size: 16px;
    padding: 10px 20px;
    border: 2px solid #ffffff;
    border-radius: 5px;
    transition: all 0.3s ease;
}

.link-back a:hover {
    background: #ffffff;
    color: #1abc9c;
}''')

print("Файлы успешно созданы с кодировкой UTF-8")
