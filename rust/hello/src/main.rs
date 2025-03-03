use actix_web::{web, App, HttpServer};
use env_logger::{Builder, Env};
use std::{
    env,
    io::{Error, ErrorKind, Result},
    num::ParseIntError,
};

mod config;
mod handler;

#[actix_web::main]
async fn main() -> Result<()> {
    Builder::from_env(Env::default().default_filter_or("info")).init();

    let port = match env::var("PORT") {
        Ok(v) => v
            .parse()
            .map_err(|e: ParseIntError| Error::new(ErrorKind::Other, e.to_string()))?,
        Err(_) => 8080,
    };

    // Create the HTTP server
    HttpServer::new(|| {
        App::new()
            .wrap(actix_web::middleware::Logger::default())
            .configure(config::configure)
            .route("/", web::get().to(handler::index))
            .route("/", web::post().to(handler::index))
    })
    .bind(("0.0.0.0", port))?
    .workers(1)
    .run()
    .await
}
