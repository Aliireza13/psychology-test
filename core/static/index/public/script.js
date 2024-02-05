// document.querySelector(".next-btn").addEventListener("click", function () {
//   document.querySelector(".question").textContent = `hello`;
// });
// document.getElementById('scrollButton').addEventListener('click', function() {
// document.getElementById("scrollButton").classList.add("active");
// setTimeout(function () {
//   document.getElementById("scrollButton").classList.remove("active");
//   window.scrollBy(0, 100);
// }, 500); // با این دو خط کد به کمک setTimeout، ما دکمه را با کلاس active ایجاد می‌کنیم و سپس آن را بعد از مدت زمان 0.5 ثانیه حذف می‌کنیم.
// document
//   .getElementById("scrollDownButton")
//   .addEventListener("click", function () {
//     const contentElement = document.getElementById("form");
//     contentElement.scrollIntoView({ behavior: "smooth" });
function scrollToNextQuestion(currentQuestionIndex) {
  const form = document.getElementById('myForm');
  const nextQuestionIndex = currentQuestionIndex + 1;
  const nextQuestion = document.getElementById('question' + nextQuestionIndex);

  if (nextQuestion) {
    nextQuestion.style.display = 'block';
    form.scrollTop = nextQuestion.offsetTop;
  } else {
    alert('No more questions.');
  }
}
for (i = 1; i < 38; i++) {
  const html = `<div
  class="form-div w-[37%] h-[350px] border-white border-x-4 border-y-0  rounded-md text-center relative pb-8"
  id="question${i}"
 
>
  
  <div
    class="w-full h-[105%] bg-slate-200 blur-md opacity-[0.87] absolute z-[-10]"
  ></div>

  <div
  id="question${i++}"
    data-question-number="1"
    class="w-[100%] text-center h-full p-2 flex flex-col items-center gap-4 mx-auto z-20"
  >
    <p
      class="w-[100%] text-center border-black border-t-2 border-b-2 font-bold mb-3 mt-2"
    >
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat at
      molestiae voluptate neque esse dshfjkdshfjkdshfdsjkf
    </p>
    <div class="flex w-[24%] justify-between pt-[39px]">
      <input type="radio" name="A" value="A" class="firstinp" />
      <label for="firstinp">A</label>
    </div>
    <div class="flex w-[24%] justify-between">
      <input type="radio" name="A" value="B" class="secondinp" />
      <label for="secondinp">B</label>
    </div>
    <div class="flex w-[24%] justify-between">
      <input type="radio" name="A" value="C" class="thridinp" />
      <label for="thridinp">C</label>
    </div>
    <div class="flex w-[24%] h-3 justify-between mb-4 last-div">
      <input type="radio" name="A" value="D" class="forthinp" />
      <label for="forthtinp">D</label>
    </div>
  </div>
  
</div>`;
  document.getElementById('myForm').insertAdjacentHTML('afterbegin', html);
  console.log(html);
}
console.log(`hello`);

const htmml = ` <div
class="form-div w-[37%] h-[350px] border-white border-x-4 border-t-4 rounded-md text-center relative pb-8"
id="question1"
>
<div
  class="w-full h-[105%] bg-slate-200 blur-md opacity-[0.87] absolute z-[-10]"
></div>

<div
  data-question-number="1"
  class="w-[100%] text-center h-full p-2 flex flex-col items-center gap-4 mx-auto z-20"
>
  <p
    class="w-[100%] text-center border-black border-t-2 border-b-2 font-bold mb-3 mt-2"
  >
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat at
    molestiae voluptate neque esse dshfjkdshfjkdshfdsjkf
  </p>
  <div class="flex w-[24%] justify-between">
    <input type="radio" name="A" value="A" class="firstinp" />
    <label for="firstinp">A</label>
  </div>
  <div class="flex w-[24%] justify-between">
    <input type="radio" name="A" value="B" class="secondinp" />
    <label for="secondinp">B</label>
  </div>
  <div class="flex w-[24%] justify-between">
    <input type="radio" name="A" value="C" class="thridinp" />
    <label for="thridinp">C</label>
  </div>
  <div class="flex w-[24%] h-3 justify-between mb-4 last-div">
    <input type="radio" name="A" value="D" class="forthinp" />
    <label for="forthtinp">D</label>
  </div>
</div>
</div>`;

document.getElementById('question37').style.borderTop = '4px solid white';
