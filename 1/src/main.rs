use std::fs::File;
use std::io::prelude::*;
use std::path::Path;

fn main() {
    let path = Path::new("input.txt");
    let display = path.display();

    let mut file = match File::open(path) {
        Ok(file) => file,
        Err(why) => panic!("couldn't open {}:{}", display, why),
    };

    let mut s = String::new();
    match file.read_to_string(&mut s) {
        Ok(_) => print!("{}", s),
        Err(why) => panic!("couldn't read {}:{}", display, why),
    }

}
