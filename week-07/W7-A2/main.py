from factory import ExporterFactory
from dataset import DATASET

def main():
    export_format = input("Enter export format type (csv/json/xml): ").lower()
    
    exporter = ExporterFactory.create_exporter(export_format)
    exporter.export(DATASET, export_format)
    
    print(f"Data exported to products.{export_format}")
    


if __name__ == "__main__":
    main()
