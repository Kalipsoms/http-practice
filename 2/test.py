
import http.client

def check(method, path):
    print(f"\nПроверка: {method} {path}")

    conn = http.client.HTTPConnection(
        "127.0.0.1", 8765, timeout=3
    )

    try:
        conn.request(method, path)
        response = conn.getresponse()

        print("Статус:", response.status, response.reason)
        print("Content-Type:", response.getheader("Content-Type"))

        response.read()

    except Exception as e:
        print("ОШИБКА:", e)

    finally:
        conn.close()


check("GET", "/index.html")
check("GET", "/abc.html")
check("POST", "/")
check("HEAD", "/style.css")
