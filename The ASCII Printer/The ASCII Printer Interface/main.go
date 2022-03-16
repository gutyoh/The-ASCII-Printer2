package main

import (
    "bufio"
    "fmt"
    "log"
    "os"
)

type FileName string

// Do not change the contents of the PrintAscii() method!
func (f FileName) PrintAscii() {
    b, err := os.ReadFile(string(f))
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(string(b))
}

// Create the AsciiPrinter interface with the PrintAscii() method below:
type ? interface {
    ?
}

func main() {
    // DO NOT delete the following line! - it creates the Ascii Art:
    createAsciiArt()

    // Create the variable 'a' of the AsciiPrinter interface type below:
    var a ?

    // Open and read the file "ascii_art.txt" with the 'a' AsciiPrinter interface:
    a = FileName("ascii_art.txt")

    // Call the PrintAscii() method on the 'a' AsciiPrinter interface below:
    a.?
}

// DO NOT DELETE! createAsciiArt() is a helper that generates the ascii art
func createAsciiArt() {
    file, err := os.Create("ascii_art.txt")
    if err != nil {
        log.Fatal(err)
    }

    scanner := bufio.NewScanner(os.Stdin)
    for i := 0; i < 14; i++ {
        scanner.Scan()
        fmt.Fprintln(file, scanner.Text())
    }
}
