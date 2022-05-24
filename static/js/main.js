let classes = ["f0", "f1", "f2", "f3", "f4"];
let classIndex = 2;

document.getElementById('aumentar').addEventListener('click', ()=>{
    let previousClass = classIndex;
    classIndex++;
    classIndex = (classIndex== classes.length) ? classes.length - 1: classIndex;
    changeClass(previousClass, classIndex ); 
});

document.getElementById('disminuir').addEventListener('click', ()=>{
    let previousClass = classIndex;
    classIndex--;
    classIndex = (classIndex < 0) ? 0 : classIndex;
    changeClass(previousClass, classIndex);
});

let changeClass = (previous, next)=>{
    if(previous != next){
        let htmlElement = document.querySelector('html');
        htmlElement.classList.remove(classes[previous]);
        htmlElement.classList.add(classes[next]);
        
    }
}
document.getElementById('restaurar').addEventListener( 'click', ()=>{
    location.reload();
});
changeClass()
const cuerpo = document.body;
document.getElementById('dark').addEventListener('click',()=>{ 
    cuerpo.classList.toggle('dark-mode');
 });