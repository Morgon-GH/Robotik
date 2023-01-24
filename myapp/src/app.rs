/// We derive Deserialize/Serialize so we can persist app state on shutdown.
#[derive(serde::Deserialize, serde::Serialize)]
#[serde(default)] // if we add new fields, give them default values when deserializing old state
pub struct TemplateApp {
}


impl Default for TemplateApp {
    fn default() -> Self {
        Self {}
    }
}

impl TemplateApp {
    /// Called once before the first frame.
    pub fn new(cc: &eframe::CreationContext<'_>) -> Self {
        // This is also where you can customized the look at feel of egui using
        // `cc.egui_ctx.set_visuals` and `cc.egui_ctx.set_fonts`.

        // Load previous app state (if any).
        // Note that you must enable the `persistence` feature for this to work.
        if let Some(storage) = cc.storage {
            return eframe::get_value(storage, eframe::APP_KEY).unwrap_or_default();
        }

        Default::default()
    }
}

impl eframe::App for TemplateApp {
    /// Called by the frame work to save state before shutdown.
    fn save(&mut self, storage: &mut dyn eframe::Storage) {
        eframe::set_value(storage, eframe::APP_KEY, self);
    }

    /// Called each time the UI needs repainting, which may be many times per second.
    /// Put your widgets into a `SidePanel`, `TopPanel`, `CentralPanel`, `Window` or `Area`.
    fn update(&mut self, ctx: &egui::Context, _frame: &mut eframe::Frame) {
        let Self {} = self;

        // Examples of how to create different panels and windows.
        // Pick whichever suits you.
        // Tip: a good default choice is to just keep the `CentralPanel`.
        // For inspiration and more examples, go to https://emilk.github.io/egui

        /*egui::SidePanel::left("side_panel").show(ctx, |ui| {
            ui.heading("Side Panel");

            ui.with_layout(egui::Layout::bottom_up(egui::Align::LEFT), |ui| {
                ui.horizontal(|ui| {
                    ui.spacing_mut().item_spacing.x = 0.0;
                    ui.label("powered by ");
                    ui.hyperlink_to("egui", "https://github.com/emilk/egui");
                    ui.label(" and ");
                    ui.hyperlink_to("eframe", "https://github.com/emilk/egui/tree/master/eframe");
                });
            });
        });*/

        egui::CentralPanel::default().show(ctx, |ui| {
            // The central panel the region left after adding TopPanel's and SidePanel's

            ui.heading("Das Sraßenspiel - Robotik Fortgeschrittene - Wirsberg Gymnasium Würzburg - Sommerfest 2022 - powered by Herr Keßelring");
            ui.hyperlink("https://github.com/la-fourier/4db.priv.strassengame-robotik");
            ui.add(egui::github_link_file!(
                "https://github.com/la-fourier/4db.priv.strassengame-robotik/tree/release-(27-07-22",
                "Software des Spielautomaten"));
            ui.add(egui::github_link_file!(
                "",
                "Vollständigen und aktuellen Berichte der Entwickler"
            ));
            ui.add(egui::github_link_file!(
                "https://github.com/la-fourier/4db.priv.strassengame-robotik/tree/app-(27-07-22)",
                "Quellcode dieser Anwendung(in Rust implementiert, zu einer '.exe' compiliert."
            ));
            egui::warn_if_debug_build(ui);
        });
        egui::Window::new("Hardware: Team Planlos über die kleinen Autos").show(ctx, |ui| {
            ui.label("'Die kleinen Autos auf der Strecke dienen als Hindernisse, welche gegen dich fahren, wenn du nicht aufpasst. Sobald eines dieser kleinen Autos gegen dich fährt, stoppt das Spiel und du hast verloren.
            Die Autos haben Reifen und eine farbige (möglichst nicht schwarz oder grau) 2x4 Platte oben drauf, um die Reifen zu verbinden. Die Farbigkeit und die Reifen geben den Autos ein etwas realistischeres Aussehen.
            Auch wurden zwei 1x2 Platten unten angebracht, um möglichst wenig Freiraum für Bewegung zu lassen. Diese potentielle Bewegung kommt davon, dass sie nur an einer Noppe festgemacht sind. Dies kommt daher, da die Straßen sehr nah aneinander sind und so nicht viel platz vorhanden ist,  um die kleinen Autos richtig zu befestigen.'
            ");
        });
        egui::Window::new("Hardware: Luca Binder über Ziele des gebauten Spieleautomatens").show(ctx, |ui| {
            ui.label("'Ziele:\n
            ⦁ 	3 „Straßen“ mit wenig Abstand\n
            ⦁ 	Möglichst wenig Spannung auf den Ketten\n
        ⦁ 	Stabilität\n
        Umsetzung:\n
        Um 3 Ketten („Straßen“) möglichst nah aneinander zu reihen, brauchten wir eine für die restlichen Straßen als Vorbild dienende Fahrbahn, um einen gleichen Aufbau bei allen drei zu erreichen. Diese Straßenkonstruktion sollte möglichst genau so breit wie die Kette sein. Die Folge daraus ist, dass der Motor unter bzw. zwischen der Kette liegen muss. Der große Motor, der für die entsprechende Geschwindigkeit sorgt, braucht mehr Platz als zwischen den Ketten unter den „normalen“ Rädern zu bieten war, weshalb eine Erhöhung für mehr Platz und weniger Spannung der 
        Ketten eingeplant wurde und ein drittes Rad auf dem die Kette läuft. Da die Erhöhung nicht zu hoch sein darf, was zu Instabilität sorgen würde, der Motor aber durch die geringe Entfernung nicht an das anzutreibende Rad anschließbar war, hatten wir die Idee, die Umdrehungen durch zwei Zahnräder an das Kettenrad weiterzuleiten. Um eine möglichst lange und stabile Straße zu bauen, darf die Kette keiner Spannung ausgesetzt sein und muss den perfekten Abstand zum Motor haben. Die Verbindung von den drei Kettentragenden Rädern muss stabil sein. Um das Gerüst möglichst stabil zu konstruieren wurden sowohl mittig als auch hinten Verstrebungen angebracht.'
        ");
        });
        egui::Window::new("Hardware: Das Pappgehäuse").show(ctx, |ui| {
            ui.label("'Die letzte Baustelle auf dem Weg zu unserem fertigen Rennspiel war der Bau des Gehäuses. 
            Dieses bauten wir mithilfe von Pappkarton und fixierten mit Klebeband. 
            Das Gehäuse ist so aufgebaut, dass es fast genau auf den Roboter zugeschnitten ist. 
            Vor der Fixierung durch Klebeband wurden die benötigten Längen gemessen und dann die Papp-Teile ausgeschnitten. Durch Messungenauigkeiten und nicht perfektes Ausschneiden, ergaben sich jedoch Probleme: Da ohnehin nicht viel Spielraum für Fehler eingeplant war, kam die Befürchtung auf, dass Seiten nicht an einander passen könnten. Diese erwies sich jedoch als eher kleinstes Übel, da nach Zusammenkleben der Seiten ein größeres Problem aufkam: 
            Durch die knapp zusammenpassenden Seiten, wurden die Autos auf der Kette an der Rückseite des Gehäuses festgehalten, wodurch sie abfielen. 
            Indem das Karton-Gehäuse so umgeändert wurde, dass es nach Außen gedrückt wird, und einer minimalen Veränderung im Design der Autos erledigte sich dieses Problem.'
            ");
        });
        egui::Window::new("Software: Leander Gundel zu der selbst implementierten Tastatur").show(ctx, |ui| {
            ui.label("'Sie kommt zum Nutzen, wenn ein Versuch/Run abgeschlossen ist. Dann kommt eine Auswahl, ob man seine Zeit mit Namen im Gerät verewigen möchte. Die Eingabe funktioniert so, dass eine QWERTZ-Schreibweisige Tastatur erscheint. Mit den Rechts-Links-Oben-Unten Tasten des Bricks wird die ausgewählte Taste gesteuert. Mit der Mittleren Taste benutzt man die derzeitig ausgewählte Taste auf dem Bildschirm. Je nach benutzter Taste erscheint der gedrückte Buchstabe oder der zuletzt gewählte Buchstabe wird gelöscht. Wenn der Name fertig ist, drückt man auf den freiliegenden Touchsensor, somit geht das Programm zum Leaderboard über.
            Nun gehen wir etwas tiefer in die Materie der Tastatur.
            Diese funktioniert so: Wir haben eine Liste mit all den Buchstaben und lassen diese einzeln ausgeben. Nun verändern wir je nach Tastendruck den Zahlenwert einer Variable. Die hilfreiche Funktion von einer Liste ist es, dass man Elemente über den jeweiligen Index abrufen kann. Somit kopieren wir über den Zahlenwert der Variable als Index den Buchstaben in einen String, den wir auf den Bildschirm ausgeben. Nachdem der Touchsensor ausgelöst hat, geben wir den String und eine weitere Variable zur Funktion Leaderboard über.'
            ");
        });
        egui::Window::new("Software: Leander Gundel über das Lea(n)derboard, die Bestenliste").show(ctx, |ui| {
            ui.label("'Erst wird geprüft, ob man aus dem Menü kommt oder einen Run abgeschlossen hat. Daraufhin werden alle erstellten Einträge(Name+Zeit) ausgelesen und sortiert. Zuletzt werden alle Einträge nacheinander ausgegeben. Ebenfalls ist es möglich, zwischen Bildschirmen mit verschiedenen Einträgen zu scrollen.
            Erst wird durch die übergebene Variable geprüft, ob ein Run abgeschlossen wurde oder man aus dem Menü kommt. Falls ein Run abgeschlossen wurde, wird ein neuer Eintrag in einer seperaten Datei, wo alle Einträge abgespeichert sind, erstellt. Danach wird die Datei ausgelesen und durch die Methode Split() in eine Liste gewandelt. Darauf werden alle zusammengehörenden Einträge durch den Modulo-operator(Rest) in eine zweidimensionale Liste(Liste in Liste) eingetragen. Dann werden alle Listen durch ihren Score in der Liste sortiert. Nun werden alle Einträge nacheinander ausgegeben. Man kann durch bestimmen, wo die Einträge zuerst ausgegeben werden(x-y-koordinaten), durch die unterschiedlichen Bildschirme scrollen.
            '");
        });
        egui::Window::new("Hintergrund: Erich Frank über unsere Vorlage").show(ctx, |ui| {
            ui.label("'Vorbild: \n- Tomy Racing Turbo cockpit (K.K. Takara Tomy)
                                  - Car cockpit  (Dickie)\n (70er-80er Vintage)\n
Als Vorbild für unser Spiel diente der Auto-
Rennspiel Simulator Tomy Racing Turbo cockpit
vom japanischen Hersteller Tomy, in welchem 
man in der Frontansicht eines Porsches anderen
Autos ausweichen musste. 
Ein wahres Highlight in jedem Kinderzimmer zur
zeit der 1980er. 
Das Rennspiel überzeugt unter anderem mit 
seinen vielen Details, so musste man bspw. 
das Spiel mit einem Zündschlüssel starten, 
woraufhin das Display hell aufleuchtete und
das eigene Auto erschien.
Durch das Einlegen einer der vier Gänge beginnt
die Straße sich mit ihren Hindernissen zu 
bewegen. Je höher der eingestellte Gang ist, 
desto schneller fährt das eigene Auto. 
Man durchfährt eine Straße, auf der andere 
Autos Hindernisse darstellen, welchen man
ausweichen muss. Links und rechts von der 
Straße sind durch grüne Streifen Wiesen angedeutet, auf welchen Bäume das Landschaftsbild bestimmen. Zudem hat das detaillierte Cockpit einen Rundenzähler, der sich mit steigender Zeitdauer des Spielens erhöht. Außerdem fallen einem Drehzahlmesser und die Geschwindigkeitsanzeige auf. 
Ein ähnliches Spielzeug veröffentlichte auch der Spielzeughersteller Dickie mit ihrem Car Cockpit, das auf Grundlage der gleichen Spielidee und Technik basiert. 
Die Besonderheit hinter der Technik beider Auto- Simulatoren besteht darin, dass sie nicht wie „normale“ Arcade- Spieleautomaten rein digital das Spiel abspielen, sondern nur mechanisch. 
Denn innerhalb der Konstruktion wird ein Band, die Straße (bei uns die Ketten), durch eine Walze angetrieben, auf welchem die Hindernisse fest befestigt sind. Das eigene Auto ist auch fest befestigt, man kann nur in unterschiedliche Richtungen steuern, also ob man rechts dem Hindernis ausweicht oder links. 
Das einzige was sich wirklich bewegt ist die Fahrbahn, also das Band, welches je nach Gang unterschiedlich schnell ist und dementsprechend den Schwierigkeitsgrad erhöht. 
'");
        });
    }
}