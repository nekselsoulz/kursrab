import requests
import logging
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Список для хранения логов
test_logs = []

def log_test_result(message):
    logger.info(message)
    test_logs.append(message)

BASE_URL = "http://localhost:5000/items"

def test_get_items():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        log_test_result("test_get_items: OK")
    else:
        log_test_result(f"test_get_items: FAILED - Status code: {response.status_code}")

def test_add_item():
    response = requests.post(BASE_URL, json={"name": "Item 1"})
    if response.status_code == 201:
        log_test_result("test_add_item: OK")
    else:
        log_test_result(f"test_add_item: FAILED - Status code: {response.status_code}")

def test_get_item():
    response = requests.get(f"{BASE_URL}/0")
    if response.status_code == 200:
        log_test_result("test_get_item: OK")
    else:
        log_test_result(f"test_get_item: FAILED - Status code: {response.status_code}")

def test_update_item():
    response = requests.put(f"{BASE_URL}/0", json={"name": "Updated Item"})
    if response.status_code == 200:
        log_test_result("test_update_item: OK")
    else:
        log_test_result(f"test_update_item: FAILED - Status code: {response.status_code}")

def test_delete_item():
    response = requests.delete(f"{BASE_URL}/0")
    if response.status_code == 200:
        log_test_result("test_delete_item: OK")
    else:
        log_test_result(f"test_delete_item: FAILED - Status code: {response.status_code}")

def test_get_nonexistent_item():
    response = requests.get(f"{BASE_URL}/999")
    if response.status_code == 404:
        log_test_result("test_get_nonexistent_item: OK")
    else:
        log_test_result(f"test_get_nonexistent_item: FAILED - Status code: {response.status_code}")

def test_update_nonexistent_item():
    response = requests.put(f"{BASE_URL}/999", json={"name": "Nonexistent"})
    if response.status_code == 404:
        log_test_result("test_update_nonexistent_item: OK")
    else:
        log_test_result(f"test_update_nonexistent_item: FAILED - Status code: {response.status_code}")

def test_delete_nonexistent_item():
    response = requests.delete(f"{BASE_URL}/999")
    if response.status_code == 404:
        log_test_result("test_delete_nonexistent_item: OK")
    else:
        log_test_result(f"test_delete_nonexistent_item: FAILED - Status code: {response.status_code}")

def test_add_multiple_items():
    for i in range(5):
        response = requests.post(BASE_URL, json={"name": f"Item {i}"})
        if response.status_code == 201:
            log_test_result(f"test_add_multiple_items (Item {i}): OK")
        else:
            log_test_result(f"test_add_multiple_items (Item {i}): FAILED - Status code: {response.status_code}")

def test_get_all_items():
    response = requests.get(BASE_URL)
    if len(response.json()['items']) == 10:
        log_test_result("test_get_all_items: OK")
    else:
        log_test_result(f"test_get_all_items: FAILED - Expected 10 items, got {len(response.json()['items'])}")

def create_pdf():
    c = canvas.Canvas("test_report.pdf", pagesize=letter)
    width, height = letter

    c.drawString(100, height - 50, "Отчет по тестам API")
    
    # Результаты тестов (лог консоли)
    c.showPage()
    c.drawString(100, height - 50, "Лог выполнения тестов:")
    
    y = height - 70
    for line in test_logs:
        c.drawString(100, y, line)
        y -= 12
    
    c.save()

if __name__ == "__main__":
    # Запуск тестов
    test_get_items()
    test_add_item()
    test_get_item()
    test_update_item()
    test_delete_item()
    test_get_nonexistent_item()
    test_update_nonexistent_item()
    test_delete_nonexistent_item()
    test_add_multiple_items()
    test_get_all_items()

    # Создание PDF отчета
    create_pdf()

