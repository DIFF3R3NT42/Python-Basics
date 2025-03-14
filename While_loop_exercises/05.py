change = float(input())


stotinki = int(change * 100)
coins_used = 0

while stotinki > 0:
    if stotinki >= 200:
        stotinki = stotinki - 200
        coins_used = coins_used + 1
    elif stotinki >= 100:
        stotinki = stotinki - 100
        coins_used = coins_used + 1
    elif stotinki >= 50:
        stotinki = stotinki - 50
        coins_used = coins_used + 1
    elif stotinki >= 20:
        stotinki = stotinki - 20
        coins_used = coins_used + 1
    elif stotinki >= 10:
        stotinki = stotinki - 10
        coins_used = coins_used + 1
    elif stotinki >= 5:
        stotinki = stotinki - 5
        coins_used = coins_used + 1
    elif stotinki >= 2:
        stotinki = stotinki - 2
        coins_used = coins_used + 1
    elif stotinki >= 1:
        stotinki = stotinki - 1
        coins_used = coins_used + 1

print(coins_used)