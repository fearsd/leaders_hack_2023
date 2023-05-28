import Card from "../../components/Card.tsx";
import Poster from "../../assets/Poster.svg";

const cardsArray = [
    {
        id: 1,
        address: "Address 1",
        title: "Title 1",
        description: "Description 1",
    },
    {
        id: 2,
        address: "Address 2",
        title: "Title 2",
        description: "Description 2",
    },
    // Остальные объекты...
    {
        id: 100,
        address: "Address 100",
        title: "Title 100",
        description: "Description 100",
    },
    {
        id: 101,
        address: "Address 101",
        title: "Title 101",
        description: "Description 101",
    },
    {
        id: 102,
        address: "Address 102",
        title: "Title 102",
        description: "Description 102",
    },
    {
        id: 103,
        address: "Address 103",
        title: "Title 103",
        description: "Description 103",
    }
];


const HomePage = () => {
    return (
        <div>
            <h1>Home Page</h1>
            <img style={{width: "100%", objectFit: "cover"}} src={Poster} alt="Poster"/>
            <div style={{display: "flex", flexDirection: "column", gap: "16px"}}>
                {cardsArray.map((card) => (
                    <Card
                        key={card.id}
                        address={card.address}
                        title={card.title}
                        description={card.description}
                        id={card.id}/>
                ))}
            </div>
        </div>
    )
}

export default HomePage
