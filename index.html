<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>실시간 럭키드로우 (데이터 저장형)</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Pretendard:wght@700;900&display=swap');
        body { 
            font-family: 'Pretendard', sans-serif; 
            touch-action: manipulation; /* 아이패드 더블탭 확대 방지 */
            user-select: none; /* 텍스트 선택 방지 */
            background-color: #f3f4f6;
        }
    </style>
</head>
<body class="py-10 px-4">

    <div class="max-w-md mx-auto">
        <div class="flex justify-between items-center mb-6">
            <h1 class="text-3xl font-black text-gray-900">LUCKY DRAW</h1>
            <button onclick="resetData()" class="text-xs text-gray-400 underline">수량 초기화(관리자)</button>
        </div>

        <div class="bg-white rounded-3xl shadow-2xl p-8 text-center mb-8 border-4 border-black">
            <div id="status-text" class="h-40 flex items-center justify-center text-xl font-bold text-gray-400">
                화면의 START를 눌러주세요!
            </div>
            
            <button id="main-btn" onclick="startDraw()" class="w-full py-6 bg-black text-white rounded-2xl text-3xl font-black shadow-lg active:scale-95 transition-all">
                START !
            </button>
        </div>

        <div class="bg-white rounded-2xl shadow-md p-6">
            <div class="flex justify-between items-center mb-4 border-b pb-2">
                <h2 class="font-bold">남은 수량 현황</h2>
                <span id="total-count" class="text-sm font-bold bg-gray-100 px-2 py-1 rounded">총 1,000개</span>
            </div>
            <div id="inventory" class="space-y-3 text-base">
                </div>
        </div>
    </div>

    <script>
        // 초기 데이터 (최초 1회만 실행됨)
        const DEFAULT_ITEMS = [
            { id: 'A', name: '바지', count: 1 },
            { id: 'B', name: '반다나', count: 9 },
            { id: 'C', name: '사인폴라로이드', count: 15 },
            { id: 'D', name: '사인앨범', count: 15 },
            { id: 'E', name: '손그림 로고 키링', count: 60 },
            { id: 'F', name: '포토카드 (1종)', count: 300 },
            { id: 'G', name: '티저 엽서', count: 600 }
        ];

        let items = [];

        // 데이터를 브라우저에서 불러오기
        function loadData() {
            const saved = localStorage.getItem('luckyDrawData');
            if (saved) {
                items = JSON.parse(saved);
            } else {
                items = [...DEFAULT_ITEMS];
                saveData();
            }
        }

        // 데이터를 브라우저에 저장하기
        function saveData() {
            localStorage.setItem('luckyDrawData', JSON.stringify(items));
        }

        // 수량 초기화 (테스트용)
        function resetData() {
            if(confirm("모든 수량을 1,000개로 다시 초기화할까요?")) {
                localStorage.removeItem('luckyDrawData');
                location.reload();
            }
        }

        function render() {
            const container = document.getElementById('inventory');
            let totalRemaining = 0;
            
            container.innerHTML = items.map(item => {
                totalRemaining += item.count;
                return `
                    <div class="flex justify-between items-center ${item.count === 0 ? 'text-gray-300 line-through' : 'text-gray-700'}">
                        <span class="font-bold">${item.id}. ${item.name}</span>
                        <span class="font-mono font-black">${item.count}</span>
                    </div>
                `;
            }).join('');

            if(totalRemaining === 0) {
                document.getElementById('main-btn').disabled = true;
                document.getElementById('main-btn').innerText = "종료";
                document.getElementById('main-btn').classList.replace('bg-black', 'bg-gray-300');
            }
        }

        function startDraw() {
            const btn = document.getElementById('main-btn');
            const status = document.getElementById('status-text');
            
            const total = items.reduce((sum, item) => sum + item.count, 0);
            if (total <= 0) return;

            btn.disabled = true;
            status.innerHTML = `<div class="animate-bounce text-black text-3xl">&#10067;</div>`;

            setTimeout(() => {
                let random = Math.floor(Math.random() * total);
                let currentSum = 0;
                let selected = null;

                for (let item of items) {
                    currentSum += item.count;
                    if (random < currentSum) {
                        selected = item;
                        item.count--;
                        break;
                    }
                }

                saveData(); // 뽑자마자 즉시 저장 (새로고침 대비)

                status.innerHTML = `
                    <div class="animate-pulse">
                        <div class="text-blue-600 text-sm font-bold mb-1">${selected.id}등급 당첨!</div>
                        <div class="text-4xl text-black font-black">${selected.name}</div>
                    </div>
                `;
                
                render();
                btn.disabled = false;
            }, 800);
        }

        // 새로고침 방지 경고창
        window.onbeforeunload = function() {
            return "진행 중인 데이터가 사라질 수 있습니다. 정말 페이지를 나가시겠습니까?";
        };

        loadData();
        render();
    </script>
</body>
</html>
