public class MyCustomException extends Exception {
    public MyCustomException(String varName,Throwable cause) {
       super("Variable " + varName + " is negative  - ",cause);
    }
    public String getMessage() {
        return super.getMessage() + getCause();
    }
} 