import { createServer } from "http";
import { Server } from "socket.io";

let httpServer = createServer();
let io = new Server(httpServer, {
    cors: {
        origin: "*"
    }
});

let scene = {
    players: {}
}

io.on("connection", (socket) => {
    

    socket.emit('init', scene)

    socket.on('join', player => {
        scene.players[player.id] = { ...player, socketId: socket.id }
        io.sockets.emit('init', scene)
    })

    socket.on('update', player => {
        scene.players[player.id] = player;
        socket.broadcast.emit('init', scene)
    })

    socket.on('disconnect', () => {
        let player = Object.values(scene.players).find(p => p.socketId == socket.id)
        if (player) delete scene.players[player.id]
        socket.broadcast.emit('init', scene)
    })
});


export let doraemonHttpServer = httpServer