from flask import Flask, render_template, request, redirect, url_for, session

import mysql.connector

from config.config import DB_CONFIG

app = Flask(__name__)
app.secret_key = "maritano_secret_key"


def get_db_connection():

    return mysql.connector.connect(
        host=DB_CONFIG["host"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        database=DB_CONFIG["database"]
    )


@app.route("/")
def home():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():

    error = None

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()

        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            """
            SELECT *
            FROM users
            WHERE username=%s
            AND password=%s
            """,
            (username, password)
        )

        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user:

            session["user"] = user["username"]

            return redirect(
                url_for("dashboard")
            )

        else:

            error = "Username atau password salah"

    return render_template(
        "login.html",
        error=error
    )


@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        user=session["user"]
    )


@app.route("/products")
def products_page():

    if "user" not in session:
        return redirect(url_for("login"))

    conn = get_db_connection()

    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM products"
    )

    products = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        "products.html",
        products=products
    )


@app.route("/add-product", methods=["GET", "POST"])
def add_product():

    if "user" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        conn = get_db_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO products
            (name, category, price, image)
            VALUES (%s, %s, %s, %s)
            """,
            (
                request.form["name"],
                request.form["category"],
                request.form["price"],
                request.form["image"]
            )
        )

        conn.commit()

        cursor.close()
        conn.close()

        return redirect(
            url_for("products_page")
        )

    return render_template(
        "add_product.html"
    )


@app.route("/edit-product/<int:id>", methods=["GET", "POST"])
def edit_product(id):

    if "user" not in session:
        return redirect(url_for("login"))

    conn = get_db_connection()

    cursor = conn.cursor(dictionary=True)

    if request.method == "POST":

        cursor.execute(
            """
            UPDATE products
            SET
                name=%s,
                category=%s,
                price=%s,
                image=%s
            WHERE id=%s
            """,
            (
                request.form["name"],
                request.form["category"],
                request.form["price"],
                request.form["image"],
                id
            )
        )

        conn.commit()

        cursor.close()
        conn.close()

        return redirect(
            url_for("products_page")
        )

    cursor.execute(
        """
        SELECT *
        FROM products
        WHERE id=%s
        """,
        (id,)
    )

    product = cursor.fetchone()

    cursor.close()
    conn.close()

    return render_template(
        "edit_product.html",
        product=product
    )


@app.route("/delete-product/<int:id>")
def delete_product(id):

    if "user" not in session:
        return redirect(url_for("login"))

    conn = get_db_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM products
        WHERE id=%s
        """,
        (id,)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return redirect(
        url_for("products_page")
    )


@app.route("/logout")
def logout():

    session.pop(
        "user",
        None
    )

    return redirect(
        url_for("login")
    )


if __name__ == "__main__":
    app.run(debug=True)