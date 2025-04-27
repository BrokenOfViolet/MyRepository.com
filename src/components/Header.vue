<template>
    <div class="header"><br>
        <span class="magic">电 影 推 荐</span><br>
        <span class="magic">Movie Recommendation</span>
        <div class="icon22">$</div>
    </div>
</template>

<style scoped>
    .header {
        position: relative;
        text-align: center;
        height: 80px;
        background-color: #f0f0f0;
        color: red;
    }
    .magic {
        width:max-content;
        font-size:24px;
        font-weight:900;
        color:transparent;
        background-clip:text;
        -webkit-background-clip:text;
        background-image:linear-gradient(97deg,#0096FF,#BB64FF 42%,#F2416B 74%,#EB7500);
    }
    .icon22{
        position: absolute;
        top: 0;
        right: 10%;
        width:72px;
        height:72px;
        line-height:72px;
        text-align:center;
        color:#daa500;
        font-size:40px;
        font-weight:900;
        background-color:#ffee00;
        border-radius:50%;
        box-shadow:inset 0 0 0 4px #ffee00,inset 0 0 0 5px #daa500;
        animation:ani-icon22 5s ease infinite;
        }
        @keyframes ani-icon22{
        0%{
        transform:rotateY(0deg);
        animation-timing-function:cubic-bezier(0.5,0,1,0.5);
        }
        50%{
        transform:rotateY(900deg);
        animation-timing-function:cubic-bezier(0,0.5,0.5,1);
        }
        100%{
        transform:rotateY(1800deg);
        animation-timing-function:cubic-bezier(0.5,0,1,0.5);
    }
}


</style>