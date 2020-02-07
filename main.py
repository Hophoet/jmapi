from fastapi import FastAPI 

#API main object
app = FastAPI()


#root endpoint
@app.get('/')
def root():
    
    return {
        'message':'Welcome on JM mobile application API'
    }