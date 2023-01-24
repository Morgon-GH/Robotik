#![warn(clippy::all, rust_2018_idioms)]
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")] // hide console window on Windows in release

mod app;
pub use app::TemplateApp;

mod backend;

mod brains;

// When compiling natively:
#[cfg(not(target_arch = "wasm32"))]
fn main() {
    // Log to stdout (if you run with `RUST_LOG=debug`).
    tracing_subscriber::fmt::init();

    let native_options = eframe::NativeOptions::default();
    eframe::run_native(
        "Das Straßenspiel - Robotik am Wirsberg-Gymnasium",
        native_options,
        Box::new(|cc| Box::new(myapp::TemplateApp::new(cc))),
    );
}
