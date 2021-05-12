# Abgabengruppierer

Dieses Python Skript automatisiert das Gruppieren der Abgaben einzelner Studenten. Die Gruppen werden dabei durch eine Excel Tabelle (z.B. Gruppeneinteilung_Kurs2_WS1920.xlsx) festgelegt.

### Voraussetzungen an die Excel Datei
- Die Excel Datei, die die Zuordnung der Studenten auf deren Gruppen enthält benötigt zwingend eine Spalte in der in beliebiger Form das u-kürzel vorhanden ist und eine weitere Spalte in der die Gruppennummer steht.
- Das Skript sucht in der Gruppenspalte nach Ganzzahlen im Bereich von 0...999. Es dürfen auch Strings, wie sie aus ILIAS kommen vorhanden sein. Bei folgendem Feldwert "Signale und Systeme - Workshop (#93)" wird die Gruppennummer 93 extrahiert.

## Getting Started

Das Skript besteht aus zwei Python Skript Dateien [main.py](./main.py) und [group_distribution.py](./group_distribution.py). Dieses kopiert die für den jeweiligen Kor­rek­tor relevanten Abgaben gemäß der Gruppenzuordnung in Gruppenordner in ein neues Verzeichnis (./Korrektur).

### Voraussetzungen

Diese Software wird zum ausführen des Skrips benötigt:

Basis Python installation: 
- [Python](https://www.python.org/)

Python Pakete: 
- [Pandas](https://pandas.pydata.org/)

Optional kann auch [Anconda](https://www.anaconda.com/) installiert werden. Hier ist bereits beides vorhanden.

Folgende Verzeichnisstruktur wird empfohlen:
```
└───WS20_21
    │   main.py
    │   group_distribution.py
    │   Gruppeneinteilung_Kurs2_WS2021.xlsx
    |   Bewertungsbogen.pdf
    │
    ├───Abgaben
    │   ├───Groß_Christoph_uzowo_1234567
    |   |      Gruppe22_Kurs2.pdf
    │   ├───Tauch_Max_uipca_7643210
    |   |      Gruppe17_Kurs2.pdf
    │   ├───Tietz_Alexandra_uprnl_3214670
    |   |       Gruppe17_Kurs2.pdf
```

### Das Skript ausführen
0. Sicher stellen, dass in [main.py](./main.py) oben im Skript die Variablen `kuerzelCol, groupCol, headerRow` den Spaltennamen der Exceldatei entsprechen. Genau darauf achten in welcher Zeile sich die Überschriften befinden. Wenn diese in Excel in der Zeile 1 sind, entpricht das `headerRow = 0`.

1. In der Konsole kann mit folgendem Befehl (Vorausgesetzt die Umgebungsvariable für das Python Verzeichnis ist vorhanden) das Skript gestartet werden.

```
python main.py
```

2. Darauf hin werden mögliche Quelldateien für die Gruppeneinteilung im .xls(x) Format, die auf der selben Verzeichnisebene wie das Skript liegen, aufgelistet. Diese können dann durch Eingabe der bevorstehenden Nummer in der Konsole ausgewählt und mit 'Enter' geladen werden.

3. Nun kann durch Konsoleneingabe der Bereich der Gruppen ausgewählt werden, die zu korrigieren sind.
Für den Fall, dass der Kor­rek­tor die Gruppen 1 bis inkl. Gruppe 17 bewerten soll:
```
1, 17
```

4. Darauf hin werden mögliche Quellverzeichnisse der Ausarbeitungen, die auf der selben Verzeichnisebene wie das Skript liegen, aufgelistet. Diese können dann durch Eingabe der bevorstehenden Nummer in der Konsole ausgewählt und mit 'Enter' geladen werden.

5. (Optional) Es kann pro Gruppe jeweils ein Bewertungsbogen in den Gruppenordner kopiert werden. Dazu muss ein noch nicht ausgefüllter Bewertungsbogen als PDF auf der selben Verzeichnisebene wie das Skript liegen. Ist dies erwünscht, kann mit 'y' bestätigt werden.

6. Auf der Verzeichnisebene des Skripts wird nun ein Ordner mit dem Namen Korrektur erstellt:

```
└───Korrektur
    ├───Gruppe_1
    |   |   Bewertungsbogen-Gruppe_1.pdf
    |   |
    │   ├───Grimmer_Bjoern_uhfel_1530223
    │   │       Gruppe001Kurs2V005.pdf
    │   │
    │   ├───Thon_Alicia_ulofg_1522686
    │   │       Gruppe001Kurs2V005.pdf
    │   │
    │   └───Lehr_Aron_uxhgz_1544773
    │           Gruppe001Kurs2V005.pdf
    │
    ├───Gruppe_2
    |   |   Bewertungsbogen-Gruppe_2.pdf
    │   │   missing_members.txt
    │   │
    │   └───Frida_Hoppe_uaxko_1542362
    │           Gruppe2_Kurs2.pdf
```

Sobald die Ausarbeitung eines oder mehrerer Gruppenmitglieder nicht im Abgaben Ordner vorliegt, diese aber in der Gruppeneinteilung Excel-Tabelle aufgelistet sind, wird im jeweilig erstelltem Gruppenordner die Datei 'missing_members.txt' erzeugt. In dieser befinden sich die U-Kürzel der Gruppenmitglieder, für die keine Abgabe vorhanden ist.

## Authors

* **Samuel Mauch** - *Initial work* - [smauch](https://github.com/smauch)
