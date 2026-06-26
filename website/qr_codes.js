// QR-Code-Inhalte
// Für jeden QR-Code eine UUID als Schlüssel eintragen.
// Felder: title, text, image (optional, URL)
const QR_CODES = {
  "001": {
    title: "Wusstest du schon?",
    text:  "Der LGV wurde 1924 gegründet und hat seitdem über 500 Mitglieder begeistert. Hier an diesem Ort fand einst das erste Sommerfest statt.",
    image: "",   // optional: URL zu einem Bild
  },
  "002": {
    title: "Bibelvers",
    text:  '„Denn ich weiß, was ich für euch plane: Pläne zum Heil und nicht zum Unheil." (Jeremia 29,11)',
    image: "",
  },
  "003": {
    title: "Historisches Foto",
    text:  "Hier siehst du ein Bild aus den Anfangsjahren des Vereins.",
    image: "https://platzhalter.example.com/foto.jpg",
  },
  // weitere QR-Codes hier einfügen ...
};
