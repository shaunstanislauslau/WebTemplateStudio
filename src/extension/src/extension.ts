import { commands, ExtensionContext, Uri, workspace, window } from "vscode";
import * as path from "path";
import { Controller } from "./controller";

export function activate(context: ExtensionContext) {
  context.subscriptions.push(
    commands.registerCommand(
      "webTemplateStudioExtension.wizardLaunch",
      async () => {
        Controller.getInstance(context, Date.now());
      }
    )
  );
  context.subscriptions.push(
    commands.registerCommand(
      "webTemplateStudioExtension.openReadme",
      async () => {
        const workspaceInfo = workspace.workspaceFolders;
        if (workspaceInfo) {
          const settingsPath = path.join(
            workspaceInfo[0].uri.fsPath,
            "README.md"
          );
          const doc = await workspace.openTextDocument(Uri.file(settingsPath));
          await window.showTextDocument(doc);
          commands.executeCommand("markdown.showPreview");
        }
      }
    )
  );
}

export function deactivate() {
  Controller.dispose();
}
