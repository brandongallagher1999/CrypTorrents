

class NewLine extends React.Component
{
    

    render()
    {
        console.log("okay");
        let list = []
        for (var i = 0; i < 6; i++)
        {
            
            list.push(<br></br>);
        }
        return(
            <div>
                {list}
            </div>
            
        );
    }
}

ReactDOM.render(<NewLine/>, document.getElementById("r_newline"));