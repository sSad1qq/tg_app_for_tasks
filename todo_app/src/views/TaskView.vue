<template>
  <div class="tasks_container">
    <div class="tasks-header">
      <input
        v-model="newTask"
        type="text"
        placeholder="Какая задача?"
        class="task-input"
        @keyup.enter="createTask"

      />
      <button @click="createTask" class="add-button">
        +
      </button>

      <div class="tasks-list">
        <div v-for="task in tasks"
        :key="task.id"
        class="task-item">
          <div class="task-text">
            {{task.title}}
          </div>
          <button class="complete-button"
          @click="completeTask(task.id)">Выполнено
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TasksView',
  data(){
    return {
      tasks: [],
      newTask: '',
    }
  },
  async mounted(){
    await this.fetchTasks()
  },
  methods: {
    async fetchTasks(){
      try{
        const tg_user = window.Telegram.WebApp.initDataUnsafe?.user
        const =
      }
    }
  }
}
</script>