from abc import ABC, abstractmethod

class DataExporter(ABC):
    @abstractmethod
    def export(self, data: list[dict], format: str):
        pass

class CSVExporter(DataExporter):    
    def export(self, data, format):
        import csv
        with open(f"products.{format}", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

class JSONExporter(DataExporter):    
    def export(self, data, format):
        import json
        with open(f"products.{format}", "w", newline="") as f:
            json.dump(data, f, indent=2)

class XMLExporter(DataExporter):
    def export(self, data, format):
        import xml.etree.ElementTree as ET