namespace py hello

service Hello
{
    string ping(1: string str);
    list<string> dozen();
}
