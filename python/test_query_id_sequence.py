
import sqlite3
from generate_demographics_queries import generate_query_id

# Create isolated in-memory database
conn = sqlite3.connect(":memory:")

# Create minimal queries table
conn.execute("""
    CREATE TABLE queries (
        query_id TEXT PRIMARY KEY
    )
""")

# Insert existing query IDs with a gap
conn.executemany("""
    INSERT INTO queries (query_id)
    VALUES (?)
""", [
    ("QRY-001",),
    ("QRY-003",)
])

# Test 1: Generate next ID
first_id = generate_query_id(conn)
print("First generated ID:", first_id)

# Simulate inserting that query
conn.execute(
    "INSERT INTO queries (query_id) VALUES (?)",
    (first_id,)
)

# Simulate deleting the query
conn.execute(
    "DELETE FROM queries WHERE query_id = ?",
    (first_id,)
)

# Test 2: Generate another ID after deletion
second_id = generate_query_id(conn)
print("ID after deletion:", second_id)

conn.close()
