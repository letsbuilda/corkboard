from pathlib import Path
import sqlite3
from typing import Optional, Dict, Any


class Database:
  def __init__(self, db_path: Path | str):
    self.db_path = db_path
    self.conn = sqlite3.connect(db_path, check_same_thread=False)
    self.conn.row_factory = sqlite3.Row
    self._configure()
    self._init_schema()

  def _configure(self):
    # Better concurrency
    self.conn.execute("PRAGMA journal_mode=WAL;")
    self.conn.execute("PRAGMA foreign_keys=ON;")

  def _init_schema(self):
    self.conn.execute("""
      CREATE TABLE IF NOT EXISTS images (
        id TEXT PRIMARY KEY,
        original_filename TEXT NOT NULL,
        stored_filename TEXT NOT NULL,
        content_type TEXT NOT NULL,
        size_bytes INTEGER NOT NULL,
        width INTEGER NOT NULL,
        height INTEGER NOT NULL,
        created_at INTEGER NOT NULL,
        deletion_token TEXT NOT NULL
      );
    """)
    self.conn.commit()

  def insert_image(self, data: Dict[str, Any]) -> None:
    self.conn.execute("""
      INSERT INTO images (
        id, original_filename, stored_filename,
        content_type, size_bytes, width, height,
        created_at, deletion_token
      ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
      data["id"],
      data["original_filename"],
      data["stored_filename"],
      data["content_type"],
      data["size_bytes"],
      data["width"],
      data["height"],
      data["created_at"],
      data["deletion_token"]
    ))
    self.conn.commit()

  def get_image(self, image_id: str) -> Optional[sqlite3.Row]:
    cursor = self.conn.execute(
      "SELECT * FROM images WHERE id = ?",
      (image_id,)
    )
    return cursor.fetchone()

  def delete_image(self, image_id: str, deletion_token: str) -> bool:
    cursor = self.conn.execute("""
      DELETE FROM images
      WHERE id = ? AND deletion_token = ?
    """, (image_id, deletion_token))
    self.conn.commit()
    return cursor.rowcount > 0

  def image_exists(self, image_id: str) -> bool:
    cursor = self.conn.execute(
      "SELECT 1 FROM images WHERE id = ?",
      (image_id,)
    )
    return cursor.fetchone() is not None