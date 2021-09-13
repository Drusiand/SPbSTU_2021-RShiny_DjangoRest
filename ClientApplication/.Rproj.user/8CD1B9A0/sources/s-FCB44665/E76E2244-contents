library(httr)
library(rlist)
library(rjson)
library(jsonlite)
library(dplyr)
library(DT)
library(shiny)

getData <- function(dbURL){
    resp<-GET(dbURL)
    jsonRespText<-content(resp,as="text") 
    dataFrame <- jsonlite::fromJSON(jsonRespText)
    return(dataFrame)
}

refreshTable <- function(output, dbURL){
    gameDataBase <- getData(dbURL)
    
    refreshedTable <- renderDataTable(
        varsExplore::datatable2(
            x=gameDataBase,
            vars = "answer",
            ) %>%
            formatStyle(names(gameDataBase),`text-align` = 'center')
        )
    return(refreshedTable)
}

difficultyChoices <- c("Easy", "Medium", "Hard")

ui <- fluidPage(
    titlePanel("Yes/No games"),
    
    shinyFeedback::useShinyFeedback(),
    
    sidebarLayout(
       sidebarPanel(
           titlePanel("Add your game:"),
           
           textInput("name", "Enter game name:"),
           radioButtons("difficulty", "Choose game difficulty", difficultyChoices),
           textAreaInput("content", "Discribe game situation"),
           textAreaInput("answer", "What's the answer?", rows=3),
           
           actionButton("add", "Add new game"),
           hr(),
           verbatimTextOutput("result")
           
        ),
        mainPanel(
            titlePanel("Available games:"),
            DT::dataTableOutput("table")
        )
    )
)

server <- function(input, output) {
    
    config <- rjson::fromJSON(file="config.json")
    
    dbURL <- config$dbURL
    
    output$table <- refreshTable(output, dbURL)
    
    observeEvent(input$add, {
        
        output$result <- renderText({
            "Some arguments missing!"
        })
        req(input$name, input$difficulty, input$content, input$answer)
        
        gameToken <- data.frame(name = input$name, 
                                difficulty = input$difficulty,
                                content = input$content,
                                answer = input$answer)
        
        jsonQuery <- rjson::toJSON(gameToken)
        
         POST(url = dbURL,
              body =  jsonQuery,
              verbose(),
              httr::add_headers(`accept` = 'application/json'), 
              httr::content_type('application/json'))
            
        output$result<- renderText({
            "New game successfully added!"
            })
        
        output$table <- refreshTable(output)
        
    })
    
}

# Run the application 
shinyApp(ui = ui, server = server)
