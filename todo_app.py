import streamlit as st

# Set page configuration
st.set_page_config(page_title="To-Do List App", page_icon="📝", layout="centered")

st.title("📝 To-Do List Web App")
st.markdown("**Stay organized and track your tasks easily!**")

# Initialize session state
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# Input new task
new_task = st.text_input("✍️ Write your task here:")

# Add new task
if st.button("➕ Add Task"):
    if new_task:
        st.session_state.tasks.append(new_task)
        st.success(f"✅ Task added: '{new_task}'")
    else:
        st.warning("⚠️ Please enter a task before adding.")

# Display tasks
st.subheader("📋 Your Tasks:")
if st.session_state.tasks:
    for i, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([8, 2])
        with col1:
            st.write(f"{i+1}. {task}")
        with col2:
            if st.button(f"❌", key=i):
                st.session_state.tasks.pop(i)
                st.experimental_rerun()
else:
    st.info("No tasks added yet! Start by adding one.")

# Footer
st.markdown("---")
st.caption("Made with ❤️ by Pooja J | Micro IT Internship Project")
