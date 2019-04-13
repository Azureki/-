package main
import "fmt"

func removeOuterParentheses(S string) string {
    res := make([]rune, 0, len(S))
    flag := 0
    for _, ch := range S{
        if ch == '(' {
            if flag != 0 {
                res = append(res, ch)
            }
            flag++
        } else {
            flag--
            if flag != 0 {
                res = append(res,ch)
            }
        }
    }
    return string(res)
}

func main(){
    S := "()()"
    res := removeOuterParentheses(S)
    fmt.Println("res:", res, ".")
}