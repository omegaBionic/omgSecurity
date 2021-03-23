package main

import (
    "fmt"
    "net/http"
    "net/url"
    "os"
    "sync"
)

func makeReq(URL string, ascii int, wg *sync.WaitGroup) {
    defer wg.Done()
    payload := string(ascii) //converting ascii value to character
    //submitting form data
    res, err := http.PostForm(URL, url.Values{
        "username": {payload},
        "password": {payload},
    })
    if err != nil {
        fmt.Println(err)
    }
    fmt.Printf("%s => %d => %s\n", payload, res.StatusCode, res.Request.URL)
}

func main() {
    var wg sync.WaitGroup
    if len(os.Args[1:]) > 1 || len(os.Args[1:]) == 0 {
        fmt.Println("ERR: one URL at a time can be passed.")
        os.Exit(0)
    }
    URL := os.Args[1:][0] //URL as command line argument
    // looping from 32 to 126 ascii values
    // I know some values are unnecessary, will fix 'em later
    for i := 32; i <= 126; i++ {
        go makeReq(URL, i, &wg)
        wg.Add(1)
    }

    wg.Wait()
}
