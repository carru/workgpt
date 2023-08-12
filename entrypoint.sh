#!/bin/bash

# Define a function to display usage instructions
usage() {
    echo "Usage: $0 <command>"
    echo "Available commands:"
    echo "  webui        Runs streamlit webserver"
    echo "  rebuild-db   Creates a new vector store and loads Confluence pages"
    echo "  append-db    Appends Confluence pages to existing vector store"
    echo "  interactive  Runs in interactive mode"
}

# Check if at least one argument is provided
if [ $# -lt 1 ]; then
    echo "Error: Please provide a command."
    usage
    exit 1
fi

# Assign the first argument to a variable
COMMAND="$1"

# Check the provided command and execute the corresponding Python script
case "$COMMAND" in
    webui)
        streamlit run webui.py
        ;;
    rebuild-db)
        rm -rf ./db/*
        python ingest_confluence.py
        ;;
    append-db)
        python ingest_confluence.py
        ;;
    interactive)
        python workgpt.py
        ;;
    *)
        echo "Error: Invalid command."
        usage
        exit 1
        ;;
esac
