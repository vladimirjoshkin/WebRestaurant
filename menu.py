import os
import sqlite3
from product import Product


PRODUCTS_DATABASE_PATH = os.path.join("databases", "products.db")


def get_product_list(lang='ru'):
    product_list = []
    # getting products
    conn = sqlite3.connect(PRODUCTS_DATABASE_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM product")
    sublist_ind = 0
    curr_elements = 0
    product_list.append([])
    for product_sql_tpl in cur.fetchall():
        if curr_elements < 4:
            product_list[sublist_ind].append(get_product(product_sql_tpl[0], lang))
            curr_elements += 1
        else:
            sublist_ind += 1
            product_list.append([])
    print(product_list)
    conn.close()
    return product_list


def get_product(product_id, lang='ru'):
    conn = sqlite3.connect(PRODUCTS_DATABASE_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM product WHERE id = ?", (product_id,))
    product_sql_tpl = cur.fetchone()
    cproduct = Product()
    cproduct.id = product_id
    cproduct.name = get_name(product_id, lang)
    cproduct.description = get_description(product_id, lang)
    cproduct.dimension = get_dimension(product_sql_tpl[1], lang)
    cproduct.default_amount = product_sql_tpl[2]
    cproduct.image_filename = product_sql_tpl[3]
    conn.close()
    return cproduct


def get_name(product_id, lang='ru'):
    conn = sqlite3.connect(PRODUCTS_DATABASE_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM translation WHERE product_id_ref = ? AND lang = ?", (product_id, lang))
    name = cur.fetchone()[3]
    conn.close()
    return name


def get_description(product_id, lang = 'ru'):
    conn = sqlite3.connect(PRODUCTS_DATABASE_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM translation WHERE product_id_ref = ? AND lang = ?", (product_id, lang))
    description = cur.fetchone()[4]
    conn.close()
    return description


def get_dimension(dimension_id, lang='ru'):
    conn = sqlite3.connect(PRODUCTS_DATABASE_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM dimension_translate WHERE dimension_ref = ? AND lang = ?", (dimension_id, lang))
    dimension = cur.fetchone()[3]
    conn.close()
    return dimension
