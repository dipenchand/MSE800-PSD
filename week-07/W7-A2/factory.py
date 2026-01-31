from exporter import CSVExporter, JSONExporter, XMLExporter

class ExporterFactory:
    @staticmethod
    def create_exporter(format_type: str):
        if format_type == "csv":
            return CSVExporter()
        elif format_type == "json":
            return JSONExporter()
        elif format_type == "xml":
            return XMLExporter()
        else:
            raise ValueError("Invalid  type")
